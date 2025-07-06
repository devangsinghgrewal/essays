.PHONY: html clean serve publish ghpages

html:
	pelican content -o output -s pelicanconf.py

clean:
	rm -rf output

serve: html
	cd output && python -m http.server 8000

publish:
	pelican content -o output -s publishconf.py

ghpages: publish
	ghp-import -m "Publish site" -n -p output 