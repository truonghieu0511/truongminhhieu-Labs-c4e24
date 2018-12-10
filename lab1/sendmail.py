from gmail import GMail , Message
from random import randint
sickness_list = ["thương hàn "," kiết lị","langben "]
i = randint(0,len(sickness_list)-1)
sickness = sickness_list[i]

html_template = '''
<p>ch&agrave;o sếp ,</p>
<p>s&aacute;ng nay em thấy m&igrave;nh mệt mỏi c&aacute;c thứ c&aacute;c thứ , b&aacute;c sĩ bảo e <strong>{{sickness}}</strong></p>
<p>xếp cho em xin nghỉ :((( !</p>
'''
html_content=html_template.replace("{{sickness}}",sickness)

gmail = GMail("truonghieu05119x@gmail.com","Truongminhhieu0511")
msg =   Message("test message", to="c4e.techkidsvn@gmail.com", html=html_content)
gmail.send(msg)