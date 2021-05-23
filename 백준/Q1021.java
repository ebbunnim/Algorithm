package 백준;

import java.util.LinkedList;
import java.util.Scanner;

public class Q1021{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt(); 
        int M = sc.nextInt();
        int cnt = 0;

        LinkedList<Integer> list = new LinkedList<>();
        for (int i=1;i<=N;i++){
            list.add(i);
        }

        while (M-->0){
            int tgt = sc.nextInt();
            while (true){
                if (list.getFirst()==tgt){
                    list.pollFirst();
                    break;
                }
                if (list.indexOf(tgt)<=list.size()/2){
                    list.addLast(list.pollFirst());
                }
                else {
                    list.addFirst(list.pollLast());
                }
                cnt++;
            }

        }
        System.out.println(cnt);
    }
}