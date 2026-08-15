class Node{
        Node links[]=new Node[26];
        boolean flag=false;
        int cntEndsWith=0;
        int cntPrefix=0;
        public Node(){}
        boolean containsKey(char ch){
            return (links[ch-'a']!=null);
        }
        void put(char ch, Node node){
            links[ch-'a']=node;
        }
        Node get(char ch){
            return links[ch-'a'];
        }
        void setEnd(){
            flag=true;
        }
        boolean isEnd(){
            return flag;
        }
        void increaseEnd(){
            cntEndsWith++;
        }
        void increasePrefix(){
            cntPrefix++;
        }
        void deleteEnd(){
            cntEndsWith--;
        }
        void reducePrefix(){
            cntPrefix--;
        }
        int getEnd(){
            return cntEndsWith;
        }
        int getPrefix(){
            return cntPrefix;
        }
}

class Trie {
    private static Node root;
    public Trie() {
        root=new Node();
    }
    
    public void insert(String word) {
        Node node=root;
        for (int i=0;i<word.length();i++){
            if (!node.containsKey(word.charAt(i))){
                node.put(word.charAt(i),new Node());
            }
            node=node.get(word.charAt(i));
            node.increasePrefix();
        }
        node.setEnd();
        node.increaseEnd();
    }
    
    public boolean search(String word) {
        Node node=root;
        for (int i=0;i<word.length();i++){
            if (!node.containsKey(word.charAt(i))){
                return false;
            }
            node=node.get(word.charAt(i));
        }
        return node.isEnd();
    }
    
    public int countWordsEqualTo(String word) {
        Node node=root;
        for (int i=0;i<word.length();i++){
            if (!node.containsKey(word.charAt(i))){
                return 0;
            }
            node=node.get(word.charAt(i));
        }
        return node.getEnd();
    }
    public int countWordsStartingWith(String word) {
        Node node=root;
        for (int i=0;i<word.length();i++){
            if (!node.containsKey(word.charAt(i))){
                return 0;
            }
            node=node.get(word.charAt(i));
        }
        return node.getPrefix();
    }
    
    public boolean startsWith(String prefix) {
        Node node=root;
        for (int i=0;i<prefix.length();i++){
            if (!node.containsKey(prefix.charAt(i))){
                return false;
            }
            node=node.get(prefix.charAt(i));
        }
        return true;
    }
    public void erase(String word){
        Node node=root;
        for (int i=0;i<word.length();i++){
            if (!node.containsKey(word.charAt(i))){
                node.put(word.charAt(i),new Node());
            }
            node=node.get(word.charAt(i));
            node.reducePrefix();
        }
        node.deleteEnd();
        }
}

/**
 * Your Trie object will be instantiated and called as such:
 * Trie obj = new Trie();
 * obj.insert(word);
 * boolean param_2 = obj.search(word);
 * boolean param_3 = obj.startsWith(prefix);
 */