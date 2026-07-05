class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> un = new HashSet<>();
        for(int i=0;i<nums.length; i++){
            if(un.contains(nums[i])){
                return true;
            }
            else{
                un.add(nums[i]);
            }
        }
        return false;
    }
}