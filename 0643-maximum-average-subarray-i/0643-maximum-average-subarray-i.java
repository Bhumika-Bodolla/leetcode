class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum=0;
        double maxSum=Integer.MIN_VALUE;
        int i=0;
        int a=0;
        while(a<nums.length){
            sum+=nums[a];
            if(a-i+1 <k){
                a++;
            }

            else if(a-i+1==k){
                maxSum=Math.max(maxSum,sum);
                sum-=nums[i];
                i++;
                a++;
            }
            
        }
        return maxSum/k;
        
    }
}