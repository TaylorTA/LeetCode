class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        
        if(flowerbed.length>=2 && flowerbed[1] == 0 && flowerbed[0] == 0){
            count++;
            flowerbed[0] = 1;
        }
        
        for(int i=1; i<flowerbed.length-1; i++){
            if(flowerbed[i-1]==0 && flowerbed[i]==0 && flowerbed[i+1]==0){
                count++;
                flowerbed[i] = 1;
            }
        }
        
        if(flowerbed.length>=2 && flowerbed[flowerbed.length-2]==0 & flowerbed[flowerbed.length-1] == 0){
            count++;
            flowerbed[flowerbed.length-1] = 1;
        }
        
        if(flowerbed.length==1 && flowerbed[0]==0){
            count++;
        }
        
        if(count>=n){
            return true;
        }else{
            return false;
        }
    }
}
