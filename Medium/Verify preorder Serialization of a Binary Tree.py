"""
JAVA practice
"""
class Solution {
    public boolean isValidSerialization(String preorder) {
        int res = 1;
        String[] pl = preorder.split(",");
        for(int i = 0; i < pl.length; i++){
            res--;
            if(res < 0){
                return false;
            };
            if(!pl[i].equals("#")){
                res += 2;
            };

        };
        // System.out.println(res);
        return res == 0;
    }
}