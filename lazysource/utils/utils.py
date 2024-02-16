def escape_html(s):
    return (s.replace("&", "&amp;")
             .replace('"', "&quot;")
             .replace("'", "&#39;"))
