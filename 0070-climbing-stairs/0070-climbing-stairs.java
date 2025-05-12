class Solution {
    public int climbStairs(int n) {
        int a=0;
        int b=1;
        if(n<=2){
            return n;
        }
        for(int i=1;i<=n;i++){
            int temp=b;
            b=a+b;
            a=temp;
        }
        return b;
    }
}