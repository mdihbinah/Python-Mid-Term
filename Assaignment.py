
class Star_Cinema :
    def __init__(self) -> None:
        self.__hall_list = []

    def entry_hall(self,hall_name):
        self.__hall_list.append(hall_name)


class Hall(Star_Cinema) :
    def __init__(self,rows,cols,hall_no) -> None:
        self.seats={}
        self.__show_list=[]
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
    
        self.seats[hall_no] = [[] * cols for _ in range(rows)]

    def entry_show(self,id, movie_name,time) :
        show_info = (id, movie_name,time)
        self.__show_list.append(show_info)
        # self.__show_list.append()

        self.seats.update({"id":[self.rows][self.cols]})

    def book_seat(self,id,__show_list):
        if 'id' in self.seats:
           seat=self.seats('id')
           flag=False
           for x in self.rows:
               for y in self.cols:
                   if(seat[x][y]==0):
                       flag=True
                       seat[x][y]=1
                       break
        if(flag==False):
               print('All seats are booked')            
        else:
           print("Error:'id' is missing.")
    def view_show_list(self,id):
       x=self.seats('id')
       for row in self.rows:
           for col in self.cols:
               print(x[row][col])

