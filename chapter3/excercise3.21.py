current_jumping = eval(input("Enter the current jump distance in meters"))
world_record = 8.85
difference = world_record - current_jumping
formatted_num = '{:.1f}'.format(difference*2)
print(f"You need to jump: {difference} additional meters to improve the world record.")
print("meters: ",round(difference,0))
