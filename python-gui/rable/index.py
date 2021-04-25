from tkinter import *   #tkinter모듈 로드

root = Tk()
root.title("PY Gui") #타이틀 지정

label1 = Label(root, text="Label") #Label이라는 텍스트를 출력합니다(창에)
label1.pack()

photo = PhotoImage(file="C:/Users/Calix/Desktop/python-gui/Button/yes.png") #사진지정 yes.png
label2 = Label(root, image=photo)
label2.pack()

def change(): #change라는 함수
    label1.config(text="Changed!") #함수 작동시 라벨1의 글자가 Changed! 로 변경

    global photo2 #사진 삭제 방지
    photo2 = PhotoImage(file="C:/Users/Calix/Desktop/python-gui/Button/no.png") #사진지정 no.png
    label2.config(image=photo2)

btn = Button(root, text="click!", command=change) #click1 이라는 버튼을 생성 위의 change함수를 버튼 클릭시 실행
btn.pack()

root.mainloop()