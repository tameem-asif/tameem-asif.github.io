import os
import markdown

if not os.path.exists('../public'):
    os.mkdir('../public')

for subdir, dirs, files in os.walk('../src/'):
    for f in files:
        with open(os.path.join(subdir, f), 'r') as file:
            raw = file.read()
            html = markdown.markdown(raw)

        file_name = os.path.basename(f)
        new_dir = subdir
        new_dir = "../public" + new_dir[6:]
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
        destination = os.path.join(new_dir,
                                   os.path.splitext(file_name)[0] + ".html")

        with open(destination, 'w+') as file:
            file.write(
                r'''<meta name="viewport" content="width=device-width, initial-scale=1">
            <link rel = "stylesheet" href="https://cdn.jsdelivr.net/gh/tameem-asif/tameem-asif.github.io@master/public/styles/markdown.css">
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
            </head>
            <body class="markdown-body">
    ''')
            file.write(html)
            file.write(r'''
    </body>
    </html>''')
