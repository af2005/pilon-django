

css_classes_to_extend = {
    #"type-h1": ".tui-heading::before"
}


with open("bootstrap-icons.css", 'r') as f:
    s = f.read()
    for new_css_class in css_classes_to_extend:
        s = s.replace(css_classes_to_extend[new_css_class], new_css_class+" ,")

with open("bootstrap-icons-patched.css", 'w') as o:
    o.write(s)

