class Solution {
    public int largestAltitude(int[] gain) {
        int p=0;
        int m=0;
        for(int i:gain)
        {
            p+=i;
            m=Math.max(m,p);
        }
        return m;
    }
}