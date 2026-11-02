class Solution {
    public int[] runningSum(int[] nums) {
        int p=0;
        int[] r=new int[nums.length];
        for(int i=0;i<nums.length;i++)
        {
            r[i]=p;
            p+=nums[i];
        }
        for(int i=0;i<nums.length-1;i++)
        {
            r[i]=r[i+1];
        }
        r[nums.length-1]=p;
        return r;
    }
}