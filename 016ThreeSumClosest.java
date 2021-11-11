class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int diff = Integer.MAX_VALUE;
        
        for(int i=0; i<nums.length; i++){
            if(i == 0 || nums[i-1] != nums[i]){
                int low = i+1;
                int high = nums.length - 1;
                while(low < high){
                    int sum = nums[i] + nums[low] + nums[high];
                    if(Math.abs(target - sum) < Math.abs(diff)){
                        diff = target - sum;
                    }else if(sum < target){
                        low++;
                    }else{
                        high--;
                    }
                }
            }
        }
        
        return target - diff;
    }
}
