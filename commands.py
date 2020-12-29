def h1(text:str):
    return '\n\t\t<h1>'+text.strip()+'</h1>'

def h2(text:str):
    return '\n\t\t<h2>'+text.strip()+'</h2>'

def h3(text:str):
    return '\n\t\t<h3>'+text.strip()+'</h3>'

def anchor(text:str):
    text=text.strip().split(' ',1)
    if len(text)>1:
        text='\n\t\t<a href="'+text[0]+'" target="_blank">'+text[1]+'</a><br/>'
    else:
        text='\n\t\t<a href="'+text[0]+'" target="_blank">'+text[0]+'</a><br/>'
    return text

def comment(text:str):
    return '\n\t\t<!--'+text.strip()+'-->'


commands={
    '#':h1,
    '##':h2,
    '###':h3,
    '=>':anchor,
    '//':comment,
    '\n':'\n\t\t<br/>',
    '_\n':'\n\t\t<hr/>',
}
