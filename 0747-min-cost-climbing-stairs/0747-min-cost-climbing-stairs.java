class Solution {
    public int minCostClimbingStairs(int[] cost) {
        int a=cost[0];
        int b=cost[1];

        for(int i=2;i<cost.length;i++){
            int current = cost[i] + Math.min(a,b);
            a=b;
            b=current;

        }
        
        return Math.min(b,a);
    }
}