# Instructions for how to use the script and style files
First off, the CSS files are taken from [this repo](https://github.com/sindresorhus/github-markdown-css). To get more updated CSS files, go there.
In the rendered markdown file (from the GitHub API), we need to add a class called `markdown-body` to (obviously) the body of the markdown. Here is an example:
```html
<head>
...head stuff...
</head>
<body class="markdown-body">
...the rendered markdown...
</body>
```
Now, in the head, I also need to add the proper sizing. GitHub uses 980px width and 45px padding, and 15px padding for mobile. This could look like this:
```html
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="github-markdown.css">
<style>
	.markdown-body {
		box-sizing: border-box;
		min-width: 200px;
		max-width: 980px;
		margin: 0 auto;
		padding: 45px;
	}

	@media (max-width: 767px) {
		.markdown-body {
			padding: 15px;
		}
	}
</style>
```
Python test:
```python
import requests
import os

def get_html(inp, out):
    with open(inp, "r") as markdown, open(out, "w") as html:
        payload = {"text": markdown.read(), "mode": "markdown"}
        html.write(requests.post("https://api.github.com/markdown", json=payload).text)

def add_css(name):
    content = ""
    with open(name, "r") as file:
        content = file.read()
    with open(name, "w") as html:
        to_write = """<head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel = "stylesheet" href="gh_style.css">
        <style>
        .markdown-body {{
        	box-sizing: border-box;
        	min-width: 200px;
        	max-width: 980px;
        	margin: 0 auto;
        	padding: 45px;
        }}

        @media (max-width: 767px) {{
        	.markdown-body {{
        		padding: 15px;
        	}}
        }}
        </style>
        </head>
        <body class="markdown-body">
        {0}
        </body>
        """.format(content)

        html.write(to_write)

if __name__=="__main__":
    md_file = input("Input file name: ")
    html_file = input("Output file name: ")
    get_html(md_file, html_file)
    add_css(html_file)

# Source for get_html: https://stackoverflow.com/questions/56588643/how-to-use-the-github-markdown-api-using-python
```
