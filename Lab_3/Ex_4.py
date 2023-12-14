def XML_Print(tag, content, **attributes):
    leftTag = f"<{tag}"
    for key, value in attributes.items():
        leftTag += f' {key}="{value}"'
    leftTag += '>'
    rightTag = f"</{tag}>"
    xmlElement = f"{leftTag}{content}{rightTag}"
    
    return xmlElement


if __name__ == '__main__':
    result = XML_Print("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
    print(result)