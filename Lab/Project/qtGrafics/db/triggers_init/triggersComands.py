
trigger_meeting_conflict = """
CREATE OR REPLACE FUNCTION meetConflictHour()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM invitations i
        JOIN meetingAppointments m ON i.meetingId = m.meetingId
        WHERE i.personId = NEW.personId
        AND tsrange(m.hour_begin, m.hour_end) && tsrange(NEW.hour_begin, NEW.hour_end)
    ) THEN
        RAISE EXCEPTION 'Conflict de programare pentru persoana cu ID % în intervalul %', NEW.personId, tsrange(NEW.hour_begin, NEW.hour_end);
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER meetConflictTrigger
BEFORE INSERT OR UPDATE ON invitations
FOR EACH ROW EXECUTE FUNCTION meetConflictHour();
"""

trigger_accounts_username_exists = """
CREATE OR REPLACE FUNCTION usernameExists()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM accountUsers WHERE username = NEW.username
    ) THEN
        RAISE EXCEPTION 'Username-ul % este deja folosit', NEW.username;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER checkUserexistenceTrigger
BEFORE INSERT ON accountUsers
FOR EACH ROW EXECUTE FUNCTION usernameExists();
"""

trigger_meeting_participant_doesn_exists = """
CREATE OR REPLACE FUNCTION checkUserDataExistence()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM personData WHERE personId = NEW.personId
    ) THEN
        RAISE EXCEPTION 'Participantul cu ID % nu exista', NEW.personId;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER checkUserDataExistenceTrigger
BEFORE INSERT OR UPDATE ON invitations
FOR EACH ROW EXECUTE FUNCTION checkUserDataExistence();
"""

trigger_meeting_after_current_date = """
CREATE OR REPLACE FUNCTION PastMeetingsAvoid()
RETURNS TRIGGER AS $$
BEGIN
    IF lower(NEW.hour_begin) < CURRENT_TIMESTAMP THEN
        RAISE EXCEPTION 'Nu se pot programa intalniri în trecut pentru intalnirea cu ID %', NEW.meetingId;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER pastMeetingTrigger
BEFORE INSERT OR UPDATE ON meetingAppointments
FOR EACH ROW EXECUTE FUNCTION PastMeetingsAvoid();
"""

trigger_meeting_duration_max = """
CREATE OR REPLACE FUNCTION meetDurationLimit()
RETURNS TRIGGER AS $$
BEGIN
    IF upper(NEW.hour_end) - lower(NEW.hour_begin) < interval '15 minutes' OR
       upper(NEW.hour_end) - lower(NEW.hour_begin) > interval '8 hours' THEN
        RAISE EXCEPTION 'Durata intalnirii nu este valida pentru intalnirea cu ID %', NEW.meetingId;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER meetTimeTrigger
BEFORE INSERT OR UPDATE ON meetingAppointments
FOR EACH ROW EXECUTE FUNCTION meetDurationLimit();
"""

trigger_meeting_exists = """
CREATE OR REPLACE FUNCTION meetExistence()
RETURNS TRIGGER AS $$
BEGIN
    IF NOT EXISTS (
        SELECT 1 FROM meetingAppointments WHERE meetingId = NEW.meetingId
    ) THEN
        RAISE EXCEPTION 'intalnirea cu ID % nu exista', NEW.meetingId;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER meetExistenceTrigger
BEFORE INSERT OR UPDATE ON invitations
FOR EACH ROW EXECUTE FUNCTION meetExistence();
"""

trigger_meeting_participant_limit = """
CREATE OR REPLACE FUNCTION participantNumberLimit()
RETURNS TRIGGER AS $$
DECLARE
    participant_limit INT := 10;
BEGIN
    IF (SELECT COUNT(*) FROM invitations WHERE meetingId = NEW.meetingId) >= participant_limit THEN
        RAISE EXCEPTION 'Limita de participanti depăsita pentru intalnirea cu ID %', NEW.meetingId;
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER participantNumberLimitTrigger
BEFORE INSERT ON invitations
FOR EACH ROW EXECUTE FUNCTION participantNumberLimit()
"""

trigger_commands = [
    trigger_meeting_conflict,
    trigger_accounts_username_exists,
    trigger_meeting_participant_doesn_exists,
    trigger_meeting_after_current_date,
    trigger_meeting_duration_max,
    trigger_meeting_exists,
    trigger_meeting_participant_limit
]
