def test_heading1:
    g = HtmlDocument()
    g.addHeading1("Hej")
    html = g.render()
    assert html == "<h1>Hej</h1>"
