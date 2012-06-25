// -------------------------------------------------------------------
// MarkDown setup, based on original markdow markitup sample.
// http://en.wikipedia.org/wiki/Markdown
// http://daringfireball.net/projects/markdown/
// -------------------------------------------------------------------
mySettings = {
	previewParserPath:	'/markdown_preview',
	onShiftEnter:		{keepDefault:false, openWith:'\n\n'},
	markupSet: [
        {name:'Heading 1', key:'1', openWith:'# ', placeHolder:'Heading 1' },
        {name:'Heading 2', key:'2', openWith:'## ', placeHolder:'Heading 2' },
        {name:'Heading 3', key:'3', openWith:'### ', placeHolder:'Heading 3' },
		{separator:'---------------' },		
		{name:'Bold', key:'B', openWith:'**', closeWith:'**'},
		{name:'Italic', key:'I', openWith:'_', closeWith:'_'},
		{separator:'---------------' },
		{name:'Bulleted List', openWith:'- ' },
		{name:'Numeric List', openWith:function(markItUp) {
			return markItUp.line+'. ';
		}},
		{separator:'---------------' },
		{name:'Picture', key:'P', replaceWith:'![[![Alternative text]!]]([![Url:!:http://]!] "[![Title]!]")'},
		{name:'Link', key:'L', openWith:'[', closeWith:']([![Url:!:http://]!] "[![Title]!]")', placeHolder:'Your text to link here...' },
		{separator:'---------------'},	
		{name:'Quotes', openWith:'> '},
		{name:'Code Block / Code', openWith:'(!(\t|!|`)!)', closeWith:'(!(`)!)'},
		{separator:'---------------'},
		{name:'Preview', call:'preview', className:"preview"}
	]
}
