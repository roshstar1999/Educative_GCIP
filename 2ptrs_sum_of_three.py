def find_sum_of_three(nums, target):
   # your code will replace this placeholder return statement
   n=len(nums)
   for i in range(n):
      nums.sort()
      lp=i+1
      hp=n-1
      while lp<hp:
         s2=nums[lp]+nums[hp]+nums[i]
         if s2==target:
            return True
         if s2<target:
            lp+=1
         else:
            hp-=1
   return False

