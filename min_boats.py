''' left and right in sorted array
while (left <= right){
    if (left == right){
        boats_number = boats_ number + 1
        break
    }
    if (people[left] + people[right] <= limit){
        right = right -1
        left = left +1
        boats_number = boats_number +1
    }
}
'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people)-1
        boats_number = 0
        
        while(left <= right):
            if(left == right):
                boats_number = boats_number + 1
                break
        
            if (people[left] + people[right] <= limit):    
                left = left +1
            
            right = right -1
            boats_number = boats_number +1

        return boats_number