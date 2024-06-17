import markdown
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from markdown.extensions.codehilite import CodeHiliteExtension
from bs4 import BeautifulSoup

class MarkdownToBBCode:
	
	@staticmethod
	def convert_code_to_bbcode(html):
		soup = BeautifulSoup(html, 'html.parser')
		for pre in soup.find_all('div', class_='codehilite'):
			code = pre.find('pre').find('code')
			language = pre.get('class')[1][len('language-'):] if 'language-' in pre.get('class')[1] else 'text'
			lexer = get_lexer_by_name(language)
			formatter = HtmlFormatter(nowrap=True)
			highlighted_code = highlight(code.string, lexer, formatter)
			pre.replace_with(f"[code={language}]{highlighted_code}[/code]")
		return str(soup)
	@staticmethod
	def markdown_to_bbcode(markdown_text):
    	# Convert Markdown to HTML with syntax highlighting
		html = markdown.markdown(markdown_text, extensions=[CodeHiliteExtension()])
		# Convert the HTML with highlighted code to BBCode
		bbcode = MarkdownToBBCode.convert_code_to_bbcode(html)
		# Additional conversion for Markdown to BBCode if needed
		bbcode = bbcode.replace('<strong>', '[b]').replace('</strong>', '[/b]')
		bbcode = bbcode.replace('<em>', '[i]').replace('</em>', '[/i]')
		bbcode = bbcode.replace('<h1>', '[size=24]').replace('</h1>', '[/size]')
		bbcode = bbcode.replace('<h2>', '[size=20]').replace('</h2>', '[/size]')
		bbcode = bbcode.replace('<h3>', '[size=16]').replace('</h3>', '[/size]')
		bbcode = bbcode.replace('<ul>', '[LIST]').replace('</ul>', '[/LIST]')
		bbcode = bbcode.replace('<ol>', '[LIST=1]').replace('</ol>', '[/LIST]')
		bbcode = bbcode.replace('<li>', '[*]').replace('</li>', '')
		
		bbcode = bbcode.replace('<p>', '').replace('</p>', '\n')
		return bbcode


