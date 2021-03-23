css_classes_to_extend = {
    "type-h1": "tui-heading",
    "type-bold": "tui-bold",
    "type-italic": "tui-italic",
    "type-strikethrough": "tui-strike",
    "hr": "tui-hrline",
    "blockquote-left": "tui-quote",
    "list-ul": "tui-ul",
    "list-ol": "tui-ol",
    "check2-circle": "tui-task",
    "text-indent-left": "tui-indent",
    "text-indent-right": "tui-outdent",
    "table": "tui-table",
    "image": "tui-image",
    "link-45deg": "tui-link",
    "code": "tui-code",
    "code-square": "tui-codeblock",
    "three-dots": "tui-more",
}

with open("bootstrap-icons.css", "r") as f:
    s = f.read()
    for old_css_class in css_classes_to_extend:
        s = s.replace(
            f".bi-{old_css_class}::before",
            f".{css_classes_to_extend[old_css_class]}::before, .bi-{old_css_class}::before",
        )

with open("bootstrap-icons-patched.css", "w") as o:
    o.write(s)
