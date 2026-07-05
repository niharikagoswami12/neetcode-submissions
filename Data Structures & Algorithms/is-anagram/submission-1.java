class Solution {
    public boolean isAnagram(String s, String t) {
      Map<Character, Integer> ms = new HashMap<>();
      Map<Character, Integer> mt = new HashMap<>();
      char[] sa = s.toCharArray();
      char[] ta = t.toCharArray();
      for(char si: sa){
        if(ms.containsKey(si)){
            ms.put(si, ms.getOrDefault(si, 0)+1);
        }
        else{
            ms.put(si, 1);
        }
      }
      for(char ti: ta){
        if(mt.containsKey(ti)){
            mt.put(ti, mt.getOrDefault(ti, 0)+1);
        }
        else{
            mt.put(ti, 1);
        }
      }
      if(!ms.equals(mt)){
        return false;
      }
      else{
        return true;
      }
    }
}
