with open("MBTI_Question.txt", "r") as Questions,  \
     open("MBTI_Type.txt", "r") as Type, \
     open("MBTI_Cognitive.txt", "r") as Cognitive:

    def select():
        while True:
            try:
                answer = (input("กรุณาเลือกคำตอบที่ตรงกับตัวคุณมากที่สุด:  "))
                if answer not in ['ก','ข']:
                    raise ValueError
                break
            except ValueError:
                print("กรุณาตอบเพียง ก หรือ ข เท่านั้น")
        return answer




    def find_type(list):
         return True if list.count('ก') > list.count('ข') else  False


    def show_line(word,textfile):
        textfile.seek(0)
        for line in textfile:
            if word in line:
                 return line



    E_I_gauge = []
    S_N_gauge = []
    T_F_gauge = []
    J_P_gauge = []
    question = 1

    print("แบบทดสอบทดสอบบุคลุกภาพ  Sixteen Personality Factors (16PF)\n")
    print("แบบทดสอบมี 70 ข้อ กรุณาเลือกคำตอบที่ตรงกับคุณมากที่สุด\n")

    #show the questions in the row
    for Question in Questions:
        Q = Question.split(",")
        for text in Q:
            print(text)
        answer = select()

        #collect each question
        if question in range (71):
            if question in (1,8,15,22,29,36,43,50,57,64): E_I_gauge.append(answer)
            elif question in (2,3,9,10,16,17,23,24,30,31,37,38,44,45,51,52,58,59,65,66): S_N_gauge.append(answer)
            elif question in (4,5,11,12,18,19,25,26,32,33,39,40,46,47,53,54,60,61,67,68): T_F_gauge.append(answer)
            else: J_P_gauge.append(answer)
            question +=  1

    #find the personality trait
    type = ''

    '''
    # your raw answers
    print("แรงขับเครื่อนภายนอก หรือ แรงขับเครื่อนภายใน",E_I_gauge)
    print("ใช้ประสาทสัมผัส หรือ ใช้สัญชาตญาณ",S_N_gauge)
    print("ใช้ความคิด หรือ ใช้ความรู้สึก",T_F_gauge)
    print("มีระเบียบแบบแผน หรือ มีความยืดหยุ่น",J_P_gauge)
    '''

    type += 'E' if find_type(E_I_gauge) else 'I'
    type += 'S' if find_type(S_N_gauge) else 'N'
    type += 'T' if find_type(T_F_gauge) else 'F'
    type += 'J' if find_type(J_P_gauge) else 'P'

    #your personality trait
    print("\nบุคคลิกภาพของคุณคือ: ", type)

    #describe your personality
    cognitive = show_line(type,Type).split(',')
    print("ลักษณะของคุณคือ : ", *cognitive[2:])

    #cognitive functions

    """
    item = ['E','I','S','N','T','F','J','P'] 

    Areana = [x for x in item if x in type] 
    Blind_Spot = [x for x in item if x not in type] 

    A = Areana 
    B = Blind_Spot 

    """ 
    print(Areana) 
    print(Blind_Spot) 
    """ 

    def cognitive_funcition(): 
        if (type[0] == 'E' and type[3] == 'P') or (type[0] == 'I' and type[3] == 'J') : 
            return A[1]+A[0], A[2]+B[0], B[2]+A[0], B[1]+B[0] 
        else: 
            return A[2]+A[0], A[1]+B[0], B[1]+A[0], B[2]+B[0] 
    """

    primary, secondary, tertiary, quaternary, = cognitive[1].split('-')
    print('กระบวนการความรู้ความเข้าใจ\n')
    print('การทำหน้าที่ลำดับที่ 1 : บทบาทหลัก เป็นสิ่งที่ถูกใช้เพื่อให้ไปสู่ความสำเร็จ\n',show_line(primary,Cognitive))
    print('การทำหน้าที่ลำดับที่ 2 : บทบาทรอง เป็นส่วนสนับบทบาทหลัก\n',show_line(secondary,Cognitive))
    print('การทำหน้าที่ลำดับที่ 3 : บทบาทที่สร้างความรำคาญใจ ควรใช้ในกิจกรรมที่ผ่อนคลาย สนุกสนาน สันทนาการ และปราศจากความเครียด\n',show_line(tertiary,Cognitive))
    print('การทำหน้าที่ลำดับที่ 4 : บทบาทที่อ่อนแอ เป็นสิ่งที่ถูกใช้ให้ได้ในสิ่งที่ได้มา\n',show_line(quaternary,Cognitive))


