class Solution {
    public boolean isAnagram(String s, String t) {
      Map<Character, Integer> ms = new HashMap<>();
      Map<Character, Integer> mt = new HashMap<>();
      char[] sa = s.toCharArray();
      char[] ta = t.toCharArray();
      for(char si: sa){
        ms.put(si, ms.getOrDefault(si, 0)+1);

      }
      for(char ti: ta){
        mt.put(ti, mt.getOrDefault(ti, 0)+1);
      }
      if(!ms.equals(mt)){
        return false;
      }
      else{
        return true;
      }
    }
}
