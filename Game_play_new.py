import copy
class Grid:
    black=[]
    white=[]
    black_pts=[]
    white_pts=[]

   
#path=path='C:\\Users\\yash\\Desktop\\PYTHON_PROGRAMS\\hw2_input.txt'
inputFile = open("input.txt")
input_type=inputFile.readline().strip()
input_color=inputFile.readline().strip()
print("Input color is ",input_color)
print(type(input_color))
#this will be a string
move_time=inputFile.readline().strip()
grid_struct=Grid()

check_list_w=[]
check_list_b=[]
r=5
for i in range(0,5):

    if i==2:
        r=4

    if i==3:
        r=3

    if i==4:
        r=2
        

    for j in range(0,r):
        check_list_b.append([i,j])

r=15
for i in range(11,16):

    if i!=15:
        r=r-1

    for j in range(r,16):

        check_list_w.append([i,j])
    

    
        

    
counter=0;
for i in range(0,16):

    line=inputFile.readline().strip()
    new_line=list(line)
    #print(new_line)
    for j in range(0,16):

        if new_line[j]== "W":

            if [i,j] in check_list_w:
                status=0
                

            else:
                status=1
            grid_struct.white.append([[i,j],status,[]])
            grid_struct.white_pts.append([i,j])

        elif new_line[j]== "B":

            if [i,j] in check_list_b:
                status=0
                counter=counter+1;

            else:
                status=1

            grid_struct.black.append([[i,j],status,[]])
            grid_struct.black_pts.append([i,j])

            
print(grid_struct.black)

#list_pt1=[] #The resultant states, when we move 1st point in one of the feasable directions


def jump_black(i):
    point_counter=0    
    while len(staack)>0:

        element=staack.pop()
        j_point=element[0]
        pri_list=[]
        
        if point_counter==0:
            element[1].append([j_point[0],j_point[1]])
            point_counter=point_counter+1
            
            
         
        
        if j_point[0]+1<=15 and [j_point[0]+1,j_point[1]] in grid_struct.black_pts or [j_point[0]+1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and [j_point[0]+2,j_point[1]] not in grid_struct.black_pts and [j_point[0]+2,j_point[1]] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]] not in stack_checklist:
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]+2,j_point[1]])
                staack.append([[j_point[0]+2,j_point[1]],pri_list])
                stack_checklist.append([j_point[0]+2,j_point[1]])
                grid_struct.black[i][2].append(["J",[j_point[0]+2,j_point[1]],pri_list])



        pri_list=[]
        if j_point[1]+1<=15 and [j_point[0],j_point[1]+1] in grid_struct.black_pts or [j_point[0],j_point[1]+1] in grid_struct.white_pts:
            
            if j_point[1]+2<=15 and [j_point[0],j_point[1]+2] not in grid_struct.black_pts and [j_point[0],j_point[1]+2] not in grid_struct.white_pts and [j_point[0],j_point[1]+2] not in stack_checklist:
                
                
                if j_point[0]==0 and j_point[1]==3:
                    print()
                    print("This is being print here")
                    print(pri_list)
                    print()
                    print()
                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0],j_point[1]+2])
                staack.append([[j_point[0],j_point[1]+2],pri_list])
                stack_checklist.append([j_point[0],j_point[1]+2])
                if j_point[0]==0 and j_point[1]==3:
                    print()
                    print("This is being print here")
                    print(pri_list)
                    print()
                    print()
                grid_struct.black[i][2].append(["J",[j_point[0],j_point[1]+2],pri_list])
                if j_point[0]==0 and j_point[1]==3:
                    print()
                    print("This is being print here")
                    print(pri_list)
                    print()
                    print()
                    

                               
                

        pri_list=[]        
        if j_point[0]+1<=15 and j_point[1]+1<=15 and [j_point[0]+1,j_point[1]+1] in grid_struct.black_pts or [j_point[0]+1,j_point[1]+1] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and j_point[1]+2<=15 and [j_point[0]+2,j_point[1]+2] not in grid_struct.black_pts and [j_point[0]+2,j_point[1]+2] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]+2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]+2,j_point[1]+2])
                staack.append([[j_point[0]+2,j_point[1]+2],pri_list])
                stack_checklist.append([j_point[0]+2,j_point[1]+2])
                grid_struct.black[i][2].append(["J",[j_point[0]+2,j_point[1]+2],pri_list])



        pri_list=[]
        if j_point[0]-1>=0 and [j_point[0]-1,j_point[1]] in grid_struct.black_pts or [j_point[0]-1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]-2>=0 and [j_point[0]-2,j_point[1]] not in grid_struct.black_pts and [j_point[0]-2,j_point[1]] not in grid_struct.white_pts and [j_point[0]-2,j_point[1]] not in stack_checklist:
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]-2,j_point[1]])
                staack.append([[j_point[0]-2,j_point[1]],pri_list])
                stack_checklist.append([j_point[0]-2,j_point[1]])
                grid_struct.black[i][2].append(["J",[j_point[0]-2,j_point[1]],pri_list])

               

        pri_list=[]
        if j_point[1]-1>=0 and [j_point[0],j_point[1]-1] in grid_struct.black_pts or [j_point[0],j_point[1]-1] in grid_struct.white_pts:
            
            if j_point[1]-2>=0 and [j_point[0],j_point[1]-2] not in grid_struct.black_pts and [j_point[0],j_point[1]-2] not in grid_struct.white_pts and [j_point[0],j_point[1]-2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0],j_point[1]-2])
                staack.append([[j_point[0],j_point[1]-2],pri_list])
                stack_checklist.append([j_point[0],j_point[1]-2])
                grid_struct.black[i][2].append(["J",[j_point[0],j_point[1]-2],pri_list])

               
# from here add cases


        pri_list=[]
        if j_point[0]-1>=0 and j_point[1]-1>=0 and [j_point[0]-1,j_point[1]-1] in grid_struct.black_pts or [j_point[0]-1,j_point[1]-1] in grid_struct.white_pts:
            
            if j_point[0]-2>=0 and j_point[1]-2>=0  and [j_point[0]-2,j_point[1]-2] not in grid_struct.black_pts and [j_point[0]-2,j_point[1]-2] not in grid_struct.white_pts and [j_point[0]-2,j_point[1]-2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]-2,j_point[1]-2])
                staack.append([[j_point[0]-2,j_point[1]-2],pri_list])
                stack_checklist.append([j_point[0]-2,j_point[1]-2])
                grid_struct.black[i][2].append(["J",[j_point[0]-2,j_point[1]-2],pri_list])

                

        pri_list=[]
        if j_point[0]+1<=15 and j_point[1]-1>=0 and [j_point[0]+1,j_point[1]-1] in grid_struct.black_pts or [j_point[0]+1,j_point[1]-1] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and j_point[1]-2>=0 and [j_point[0]+2,j_point[1]-2] not in grid_struct.black_pts and [j_point[0]+2,j_point[1]-2] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]-2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]+2,j_point[1]-2])
                staack.append([[j_point[0]+2,j_point[1]-2],pri_list])
                stack_checklist.append([j_point[0]+2,j_point[1]-2])
                grid_struct.black[i][2].append(["J",[j_point[0]+2,j_point[1]-2],pri_list])

               



        pri_list=[]
        if j_point[0]-1>=0 and j_point[1]+1<=15  and [j_point[0]-1,j_point[1]+1] in grid_struct.black_pts or [j_point[0]-1,j_point[1]+1] in grid_struct.white_pts:
            
            if j_point[0]-2>=0 and j_point[1]+2<=15 and [j_point[0]-2,j_point[1]+2] not in grid_struct.black_pts and [j_point[0]-2,j_point[1]+2] not in grid_struct.white_pts and [j_point[0]-2,j_point[1]+2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]-2,j_point[1]+2])
                staack.append([[j_point[0]-2,j_point[1]+2],pri_list])
                stack_checklist.append([j_point[0]-2,j_point[1]+2])
                grid_struct.black[i][2].append(["J",[j_point[0]-2,j_point[1]+2],pri_list])

               
        

            

##def Jumping_Pawn_Moves(position,overall_path):
##        movements=list()
##        range1=list(range(-1, 2))
##        range2=list(range(-1, 2))
##        for r1 in range1:
##            for r2 in range2:
##              if(r1!=0 and r2!=0):
##                position_1 = position[0]+2*r1
##                position_2 = position[1]+2*r2
##                if((position_1 >0 or position_1 < 15 or position_2 > 0 or position_2 < 15) and (board[position_1][position_2] != 'B' or board[position_1][position_2] != 'W')):
##                        previous_1= position[0]+r1
##                        previous_2 = position[1]+r2
##                        if(previous_1 >0 or previous_1 < 15 or previous_2 > 0 or previous_2 < 15):
##                          if(board[previous_1][previous_2] == 'B' or board[previous_1][previous_2] == 'W'):
##                            l=[position_1,position_2]
##                            if (not(l in overall_path)):
##                                overall_path.append([position[0],position[1]])
##                                overall_path.append([previous_1,previous_2])
##                                jumps = Jumping_Pawn_Moves([previous_1,previous_2],overall_path)[0]
##                                for a in jumps:
##                                    movements.append(a)
##                                movements.append([previous_1,previous_2])
##        return (movements,overall_path)

def jump_white(i):
    point_counter=0    
    while len(staack)>0:

        element=staack.pop()
        j_point=element[0]
        pri_list=[]
        
        if point_counter==0:
            element[1].append([j_point[0],j_point[1]])
            point_counter=point_counter+1
            
            
         
        
        if j_point[0]+1<=15 and [j_point[0]+1,j_point[1]] in grid_struct.black_pts or [j_point[0]+1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and [j_point[0]+2,j_point[1]] not in grid_struct.black_pts and [j_point[0]+2,j_point[1]] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]] not in stack_checklist:
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]+2,j_point[1]])
                staack.append([[j_point[0]+2,j_point[1]],pri_list])
                stack_checklist.append([j_point[0]+2,j_point[1]])
                grid_struct.white[i][2].append(["J",[j_point[0]+2,j_point[1]],pri_list])



        pri_list=[]
        if j_point[1]+1<=15 and [j_point[0],j_point[1]+1] in grid_struct.black_pts or [j_point[0],j_point[1]+1] in grid_struct.white_pts:
            
            if j_point[1]+2<=15 and [j_point[0],j_point[1]+2] not in grid_struct.black_pts and [j_point[0],j_point[1]+2] not in grid_struct.white_pts and [j_point[0],j_point[1]+2] not in stack_checklist:
                
                
                if j_point[0]==0 and j_point[1]==3:
                    print()
                    print("This is being print here")
                    print(pri_list)
                    print()
                    print()
                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0],j_point[1]+2])
                staack.append([[j_point[0],j_point[1]+2],pri_list])
                stack_checklist.append([j_point[0],j_point[1]+2])
                if j_point[0]==0 and j_point[1]==3:
                    print()
                    print("This is being print here")
                    print(pri_list)
                    print()
                    print()
                grid_struct.white[i][2].append(["J",[j_point[0],j_point[1]+2],pri_list])
                if j_point[0]==0 and j_point[1]==3:
                    print()
                    print("This is being print here")
                    print(pri_list)
                    print()
                    print()
                    

                               
                

        pri_list=[]        
        if j_point[0]+1<=15 and j_point[1]+1<=15 and [j_point[0]+1,j_point[1]+1] in grid_struct.black_pts or [j_point[0]+1,j_point[1]+1] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and j_point[1]+2<=15 and [j_point[0]+2,j_point[1]+2] not in grid_struct.black_pts and [j_point[0]+2,j_point[1]+2] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]+2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]+2,j_point[1]+2])
                staack.append([[j_point[0]+2,j_point[1]+2],pri_list])
                stack_checklist.append([j_point[0]+2,j_point[1]+2])
                grid_struct.white[i][2].append(["J",[j_point[0]+2,j_point[1]+2],pri_list])



        pri_list=[]
        if j_point[0]-1>=0 and [j_point[0]-1,j_point[1]] in grid_struct.black_pts or [j_point[0]-1,j_point[1]] in grid_struct.white_pts:
            
            if j_point[0]-2>=0 and [j_point[0]-2,j_point[1]] not in grid_struct.black_pts and [j_point[0]-2,j_point[1]] not in grid_struct.white_pts and [j_point[0]-2,j_point[1]] not in stack_checklist:
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]-2,j_point[1]])
                staack.append([[j_point[0]-2,j_point[1]],pri_list])
                stack_checklist.append([j_point[0]-2,j_point[1]])
                grid_struct.white[i][2].append(["J",[j_point[0]-2,j_point[1]],pri_list])

               

        pri_list=[]
        if j_point[1]-1>=0 and [j_point[0],j_point[1]-1] in grid_struct.black_pts or [j_point[0],j_point[1]-1] in grid_struct.white_pts:
            
            if j_point[1]-2>=0 and [j_point[0],j_point[1]-2] not in grid_struct.black_pts and [j_point[0],j_point[1]-2] not in grid_struct.white_pts and [j_point[0],j_point[1]-2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0],j_point[1]-2])
                staack.append([[j_point[0],j_point[1]-2],pri_list])
                stack_checklist.append([j_point[0],j_point[1]-2])
                grid_struct.white[i][2].append(["J",[j_point[0],j_point[1]-2],pri_list])

               
# from here add cases


        pri_list=[]
        if j_point[0]-1>=0 and j_point[1]-1>=0 and [j_point[0]-1,j_point[1]-1] in grid_struct.black_pts or [j_point[0]-1,j_point[1]-1] in grid_struct.white_pts:
            
            if j_point[0]-2>=0 and j_point[1]-2>=0  and [j_point[0]-2,j_point[1]-2] not in grid_struct.black_pts and [j_point[0]-2,j_point[1]-2] not in grid_struct.white_pts and [j_point[0]-2,j_point[1]-2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]-2,j_point[1]-2])
                staack.append([[j_point[0]-2,j_point[1]-2],pri_list])
                stack_checklist.append([j_point[0]-2,j_point[1]-2])
                grid_struct.white[i][2].append(["J",[j_point[0]-2,j_point[1]-2],pri_list])

                

        pri_list=[]
        if j_point[0]+1<=15 and j_point[1]-1>=0 and [j_point[0]+1,j_point[1]-1] in grid_struct.black_pts or [j_point[0]+1,j_point[1]-1] in grid_struct.white_pts:
            
            if j_point[0]+2<=15 and j_point[1]-2>=0 and [j_point[0]+2,j_point[1]-2] not in grid_struct.black_pts and [j_point[0]+2,j_point[1]-2] not in grid_struct.white_pts and [j_point[0]+2,j_point[1]-2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]+2,j_point[1]-2])
                staack.append([[j_point[0]+2,j_point[1]-2],pri_list])
                stack_checklist.append([j_point[0]+2,j_point[1]-2])
                grid_struct.white[i][2].append(["J",[j_point[0]+2,j_point[1]-2],pri_list])

               



        pri_list=[]
        if j_point[0]-1>=0 and j_point[1]+1<=15  and [j_point[0]-1,j_point[1]+1] in grid_struct.black_pts or [j_point[0]-1,j_point[1]+1] in grid_struct.white_pts:
            
            if j_point[0]-2>=0 and j_point[1]+2<=15 and [j_point[0]-2,j_point[1]+2] not in grid_struct.black_pts and [j_point[0]-2,j_point[1]+2] not in grid_struct.white_pts and [j_point[0]-2,j_point[1]+2] not in stack_checklist:
                
                

                base=element[1]
                pri_list=copy.deepcopy(base)
                pri_list.append([j_point[0]-2,j_point[1]+2])
                staack.append([[j_point[0]-2,j_point[1]+2],pri_list])
                stack_checklist.append([j_point[0]-2,j_point[1]+2])
                grid_struct.white[i][2].append(["J",[j_point[0]-2,j_point[1]+2],pri_list])







                
max_eval=float("-inf")

max_list=[]
if input_color=="BLACK":

    
    for i in range(0,19):
        
        status=grid_struct.black[i][1]
        b_point=grid_struct.black[i][0]

        if b_point[0]+1<=15 :
        
            if [b_point[0]+1,b_point[1]] not in grid_struct.black_pts and [b_point[0]+1,b_point[1]] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]+1,b_point[1]]])


        if b_point[1]+1<=15 :
        
            if [b_point[0],b_point[1]+1] not in grid_struct.black_pts and [b_point[0],b_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0],b_point[1]+1]])


        if b_point[0]+1<=15 and b_point[1]+1<=15:
        
            if [b_point[0]+1,b_point[1]+1] not in grid_struct.black_pts and [b_point[0]+1,b_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]+1,b_point[1]+1]])


        if b_point[0]-1>=0:
        
            if [b_point[0]-1,b_point[1]] not in grid_struct.black_pts and [b_point[0]+1,b_point[1]] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]-1,b_point[1]]])


        if b_point[1]-1>=0:
        
            if [b_point[0],b_point[1]-1] not in grid_struct.black_pts and [b_point[0],b_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0],b_point[1]-1]])


        if b_point[0]+1<=15 and b_point[1]-1>=0:
        
            if [b_point[0]+1,b_point[1]-1] not in grid_struct.black_pts and [b_point[0]+1,b_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]+1,b_point[1]-1]])


        if b_point[0]-1>=0 and b_point[1]+1<=15:
        
            if [b_point[0]-1,b_point[1]+1] not in grid_struct.black_pts and [b_point[0]-1,b_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]-1,b_point[1]+1]])


        if b_point[0]-1>=0 and b_point[1]-1>=0:
        
            if [b_point[0]-1,b_point[1]-1] not in grid_struct.black_pts and [b_point[0]-1,b_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[b_point[0]-1,b_point[1]-1]])


        staack=[]
        stack_checklist=[]   
        staack.append([b_point,[]])
        stack_checklist.append(b_point)
        jump_black(i)



    black_in_empty_white_o=0
    for i in range(0,19):
        if grid_struct.black_pts[i] in check_list_w:
            black_in_empty_white_o=black_in_empty_white_o+1
    number_empty_white_o=0
    for i in range(0,19):
        if check_list_w[i] not in grid_struct.black_pts and check_list_w[i] not in grid_struct.white_pts:
            number_empty_white_o=number_empty_white_o+1
            
    white_in_empty_black_o=0
    for i in range(0,19):
        if grid_struct.white_pts[i] in check_list_b:
            white_in_empty_black_o=white_in_empty_black_o+1
    number_empty_black_o=0
    for i in range(0,19):
        if check_list_b[i] not in grid_struct.black_pts and check_list_b[i] not in grid_struct.white_pts:
            number_empty_black_o=number_empty_black_o+1
    number_black_original_o=0
    for i in range(0,19):
        if grid_struct.black_pts[i] in check_list_b:
            number_black_original_o=number_black_original_o+1
            
    centroid=0
   
    for i in range(0,19):
        
        for coin in grid_struct.black[i][2]:

            #print(coin)

            black_in_empty_white=black_in_empty_white_o
            number_empty_white=number_empty_white_o
            white_in_empty_black=white_in_empty_black_o
            number_empty_black=number_empty_black_o
            number_black_original=number_black_original_o
            centroid=0
            
            #print("This is coin", coin)

            if grid_struct.black[i][1]==0:

                if coin[1] in check_list_w:
                    number_empty_white=number_empty_white-1
                    black_in_empty_white=black_in_empty_white+1
                    number_black_original=number_black_original-1
                    number_empty_black=number_empty_black+1

                elif coin[1] not in check_list_w and coin[1] not in check_list_b:
                    number_black_original=number_black_original-1
                    number_empty_black=number_empty_black+1
                    


            elif grid_struct.black[i][1]==1:

                if grid_struct.black[i][0] not in check_list_w:

                    if coin[1] in check_list_w:

                        number_empty_white=number_empty_white-1
                        black_in_empty_white=black_in_empty_white+1

                    elif coin[1] in check_list_b:

                        number_black_original=number_black_original+1
                        number_empty_black=number_empty_black-1
                        

                        

                elif grid_struct.black[i][0] in check_list_w:

                    if coin[1] not in check_list_w and coin[1] not in check_list_b :

                        number_empty_white=number_empty_white+1
                        black_in_empty_white=black_in_empty_white-1

                    elif coin[1] in check_list_b:

                        number_empty_white=number_empty_white+1
                        black_in_empty_white=black_in_empty_white-1
                        number_black_original=number_black_original+1
                        number_empty_black=number_empty_black-1

            #print("black_in_empty_white ",black_in_empty_white)
            #print("number_empty_white",number_empty_white)
            #print("white_in_empty_black",white_in_empty_black)
            #print("number_empty_black",number_empty_black)
            #print("number_black_original",number_black_original)
            #print("centroid",centroid)
                
            for j in  grid_struct.black_pts:

                centroid=centroid+((j[0]-15)**2 + (j[1]-15)**2)**0.5
            pott=grid_struct.black[i][0]
            centroid=centroid-((pott[0]-15)**2 + (pott[1]-15)**2)**0.5
            centroid=centroid+((coin[1][0]-15)**2 + (coin[1][1]-15)**2)**0.5


            if number_empty_white==0:
                eval_score=(-1000*(white_in_empty_black/number_empty_black))- number_black_original*10000-centroid
                #print(eval_score)
                

            elif number_empty_black==0:
                eval_score=(black_in_empty_white/number_empty_white)*1000 - number_black_original*10000-centroid
                #print(eval_score)

            elif number_empty_white==0 and number_empty_black==0:
                eval_score= (number_black_original*(-10000))-centroid
                #print(eval_score)

            else:
                eval_score=(black_in_empty_white/number_empty_white)*1000 + (-1000*(white_in_empty_black/number_empty_black)) - number_black_original*10000-centroid
                #print(eval_score)
            #print("The max_eval value is",max_eval)
            if eval_score>=max_eval:
                max_eval=eval_score
                print("We entered the if loop")
                #print("The  max_value inside loop is",max_eval)
                if coin[0]=="E":
                    max_list=[]
                    max_list.append("E")
                    pint=grid_struct.black[i][0]
                    
                    #print("pint is ",pint)
                    
                    max_list.append(pint)
                    #print("coin[1] is",coin[1])
                    max_list.append(coin[1])
                    #print("max_list",max_list)
                    print("The max_list inside E loop is ",max_list)
                    

                elif coin[0]=="J":

                    max_list=[]
                    #print("the value of coin[2] ",coin[2])
                    max_list=coin[2]
                    max_list.insert(0,"J")
                    #print("The max_list inside J loop is ",max_list)
                    print("The max_list inside J loop is ",max_list)


    print(max_eval)
    print(max_list)
    outputfile = open('C:\\Users\\yash\\Desktop\\PYTHON_PROGRAMS\\\\output_hw2.txt', 'w')
    outputfile.write("")
    if max_list[0]=="E":

        outputfile.write("E "+str(max_list[1][1])+","+str(max_list[1][0])+" "+str(max_list[2][1])+","+str(max_list[2][0]))
       
            
    elif max_list[0]=="J":

        for p in range(0,len(max_list)-2):

            outputfile.write("J "+str(max_list[p+1][1])+","+str(max_list[p+1][0])+" "+str(max_list[p+2][1])+","+str(max_list[p+2][0]))
            outputfile.write("\n")

        
            


    outputfile.close()
                
                





if input_color=="WHITE":

    
    for i in range(0,19):
        
        status=grid_struct.white[i][1]
        w_point=grid_struct.white[i][0]

        if w_point[0]+1<=15 :
        
            if [w_point[0]+1,w_point[1]] not in grid_struct.black_pts and [w_point[0]+1,w_point[1]] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[w_point[0]+1,w_point[1]]])


        if w_point[1]+1<=15 :
        
            if [w_point[0],w_point[1]+1] not in grid_struct.black_pts and [w_point[0],w_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[w_point[0],w_point[1]+1]])


        if w_point[0]+1<=15 and w_point[1]+1<=15:
        
            if [w_point[0]+1,w_point[1]+1] not in grid_struct.black_pts and [w_point[0]+1,w_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[w_point[0]+1,w_point[1]+1]])


        if w_point[0]-1>=0:
        
            if [w_point[0]-1,w_point[1]] not in grid_struct.black_pts and [w_point[0]+1,w_point[1]] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[w_point[0]-1,w_point[1]]])


        if w_point[1]-1>=0:
        
            if [w_point[0],w_point[1]-1] not in grid_struct.black_pts and [w_point[0],w_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[w_point[0],w_point[1]-1]])


        if w_point[0]+1<=15 and w_point[1]-1>=0:
        
            if [w_point[0]+1,w_point[1]-1] not in grid_struct.black_pts and [w_point[0]+1,w_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[w_point[0]+1,w_point[1]-1]])


        if w_point[0]-1>=0 and w_point[1]+1<=15:
        
            if [w_point[0]-1,w_point[1]+1] not in grid_struct.black_pts and [w_point[0]-1,w_point[1]+1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[w_point[0]-1,w_point[1]+1]])


        if w_point[0]-1>=0 and w_point[1]-1>=0:
        
            if [w_point[0]-1,w_point[1]-1] not in grid_struct.black_pts and [w_point[0]-1,w_point[1]-1] not in grid_struct.white_pts:
                
                grid_struct.black[i][2].append(["E",[w_point[0]-1,w_point[1]-1]])


        staack=[]
        stack_checklist=[]   
        staack.append([w_point,[]])
        stack_checklist.append(w_point)
        jump_white(i)



    black_in_empty_white_o=0
    for i in range(0,19):
        if grid_struct.black_pts[i] in check_list_w:
            black_in_empty_white_o=black_in_empty_white_o+1
    number_empty_white_o=0
    for i in range(0,19):
        if check_list_w[i] not in grid_struct.black_pts and check_list_w[i] not in grid_struct.white_pts:
            number_empty_white_o=number_empty_white_o+1
            
    white_in_empty_black_o=0
    for i in range(0,19):
        if grid_struct.white_pts[i] in check_list_b:
            white_in_empty_black_o=white_in_empty_black_o+1
    number_empty_black_o=0
    for i in range(0,19):
        if check_list_b[i] not in grid_struct.black_pts and check_list_b[i] not in grid_struct.white_pts:
            number_empty_black_o=number_empty_black_o+1
    number_white_original_o=0
    for i in range(0,19):
        if grid_struct.white_pts[i] in check_list_w:
            number_white_original_o=number_white_original_o+1
            
    centroid=0
   
    for i in range(0,19):
        
        for coin in grid_struct.white[i][2]:

            #print(coin)

            black_in_empty_white=black_in_empty_white_o
            number_empty_white=number_empty_white_o
            white_in_empty_black=white_in_empty_black_o
            number_empty_black=number_empty_black_o
            number_white_original=number_white_original_o
            centroid=0
            
            #print("This is coin", coin)

            if grid_struct.white[i][1]==0:

                if coin[1] in check_list_b:
                    number_empty_white=number_empty_white+1
                    white_in_empty_black=white_in_empty_black+1
                    number_white_original=number_white_original-1
                    number_empty_black=number_empty_black-1

                elif coin[1] not in check_list_w and coin[1] not in check_list_b:
                    number_white_original=number_white_original-1
                    number_empty_white=number_empty_white+1
                    


            elif grid_struct.white[i][1]==1:

                if grid_struct.white[i][0] not in check_list_b:

                    if coin[1] in check_list_b:

                        number_empty_black=number_empty_black-1
                        white_in_empty_black=white_in_empty_black+1

                    elif coin[1] in check_list_w:

                        number_white_original=number_white_original+1
                        number_empty_white=number_empty_white-1
                        

                        

                elif grid_struct.white[i][0] in check_list_b:

                    if coin[1] not in check_list_w and coin[1] not in check_list_b :

                        number_empty_black=number_empty_black+1
                        white_in_empty_black=white_in_empty_black-1

                    elif coin[1] in check_list_w:

                        number_empty_black=number_empty_black+1
                        white_in_empty_black=white_in_empty_black-1
                        number_white_original=number_white_original+1
                        number_empty_white=number_empty_white-1

            #print("black_in_empty_white ",black_in_empty_white)
            #print("number_empty_white",number_empty_white)
            #print("white_in_empty_black",white_in_empty_black)
            #print("number_empty_black",number_empty_black)
            #print("number_black_original",number_black_original)
            #print("centroid",centroid)
                
            for j in  grid_struct.white_pts:

                centroid=centroid+((j[0]-0)**2 + (j[1]-0)**2)**0.5
            pott=grid_struct.white[i][0]
            centroid=centroid-((pott[0]-0)**2 + (pott[1]-0)**2)**0.5
            centroid=centroid+((coin[1][0]-0)**2 + (coin[1][1]-0)**2)**0.5


            if number_empty_black==0:
                eval_score=(-1000*(black_in_empty_white/number_empty_white))- number_white_original*10000-centroid
                #print(eval_score)
                

            elif number_empty_white==0:
                eval_score=(white_in_empty_black/number_empty_black)*1000 - number_white_original*10000-centroid
                #print(eval_score)

            elif number_empty_white==0 and number_empty_black==0:
                eval_score= (number_white_original*(-10000))-centroid
                #print(eval_score)

            else:
                eval_score=(white_in_empty_black/number_empty_black)*1000 + (-1000*(black_in_empty_white/number_empty_white)) - number_white_original*10000-centroid
                #print(eval_score)
            #print("The max_eval value is",max_eval)
            if eval_score>=max_eval:
                max_eval=eval_score
                
                #print("The  max_value inside loop is",max_eval)
                if coin[0]=="E":
                    max_list=[]
                    max_list.append("E")
                    pint=grid_struct.black[i][0]
                    
                    #print("pint is ",pint)
                    
                    max_list.append(pint)
                    #print("coin[1] is",coin[1])
                    max_list.append(coin[1])
                    print("max_list",max_list)
                    #print("The max_list inside E loop is ",max_list)
                    

                elif coin[0]=="J":

                    max_list=[]
                    #print("the value of coin[2] ",coin[2])
                    max_list=coin[2]
                    max_list.insert(0,"J")
                    #print("The max_list inside J loop is ",max_list)                        

                        


    outputfile = open('output.txt', 'w')
    outputfile.write("")
    if max_list[0]=="E":

        outputfile.write("E "+str(max_list[1][1])+","+str(max_list[1][0])+" "+str(max_list[2][1])+","+str(max_list[2][0]))
        
            
    elif max_list[0]=="J":

        for p in range(0,len(max_list)-2):

            outputfile.write("J "+str(max_list[p+1][1])+","+str(max_list[p+1][0])+" "+str(max_list[p+2][1])+","+str(max_list[p+2][0]))
            outputfile.write("\n")

        
            


    outputfile.close()
                        

                        

                

                    

                
                    
                    
                
                
                

            
                
            

            
           
#print()
#print()
#print(grid_struct.black)





                            

                            

                    


                

                    
                

            
                

        
        

    
