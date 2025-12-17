class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0;
        int tens = 0;
        int twentys = 0;
        for (int bill : bills){
            if (bill == 5){
                five++;
            }
            else if (bill == 10){
                five--;
                tens++;
            }
            else{
                tens --;
                five--;
                twentys++;
                if (five > 1 && tens < 0){
                    five -= 2;
                    tens++;
                }
            if (tens < 0 && five < 0 && twentys < 0){
                return false;
                }
            }
        }
        return true;
    }
};