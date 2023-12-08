import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;

enum Suit {
    A(14),
    K(13),
    Q(12),
    J(11),
    T(10);

    private int value;

    private Suit(int value) {
        this.value = value;
    }

    public int getValue() {
        return value;
    }
}

class Hand implements Comparable<Hand> {
    public String cards;
    public int bid;
    public int majorNum;

    public Hand(String cards, int bid) {
        this.cards = cards;
        this.bid = bid;
        this.majorNum = calculateMajorNum();
    }

    @Override
    public String toString() {
        return "cards: "+cards + " bid: " + bid + " type: " + majorNum;
    }

    private int calculateMajorNum() {
        int countOfLetter[] = new int[15];
        for (int i = 0; i < cards.length(); i++) {
            char c = cards.charAt(i);
            if (c == 'A') {
                countOfLetter[Suit.A.getValue()]++;
            } else if (c == 'K') {
                countOfLetter[Suit.K.getValue()]++;
            } else if (c == 'Q') {
                countOfLetter[Suit.Q.getValue()]++;
            } else if (c == 'J') {
                countOfLetter[Suit.J.getValue()]++;
            } else if (c == 'T') {
                countOfLetter[Suit.T.getValue()]++;
            } else {
                countOfLetter[Character.getNumericValue(c)]++;
            }
        }
        int count[] = new int[6];

        for (int i : countOfLetter) {
            count[i]++;
        }

        if (count[5] == 1) {
            return 7;
        } else if (count[4] == 1) {
            return 6;
        } else if (count[3] == 1 && count[2] == 1) {
            return 5;
        } else if (count[3] == 1) {
            return 4;
        } else if (count[2] == 2) {
            return 3;
        } else if (count[2] == 1) {
            return 2;
        } else {
            return 1;
        }

    }

    @Override
    public int compareTo(Hand arg0) {

        if (this.majorNum > arg0.majorNum) {
            return 1;
        } else if (this.majorNum < arg0.majorNum) {
            return -1;
        }

        for (int i = 0; i < this.cards.length(); i++) {
            int c1 = getSuitValue(this.cards.charAt(i));
            int c2 = getSuitValue(arg0.cards.charAt(i));
            if (c1 > c2) {
                return 1;
            } else if (c1 < c2) {
                return -1;
            }
        }
        return 0;
    }

    private static int getSuitValue(char c) {
        if (c == 'A') {
            return Suit.A.getValue();
        } else if (c == 'K') {
            return Suit.K.getValue();
        } else if (c == 'Q') {
            return Suit.Q.getValue();
        } else if (c == 'J') {
            return Suit.J.getValue();
        } else if (c == 'T') {
            return Suit.T.getValue();
        } else {
            return Character.getNumericValue(c);
        }
    }

}

public class day7p1 {

    public static void main(String[] args) throws IOException {
        ArrayList<Hand> hands = new ArrayList<Hand>();
        
        File file = new File("input.txt");

        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        while ((st = br.readLine()) != null) {
            String[] cards = st.split(" ");
            int bid = Integer.parseInt(cards[1]);
            hands.add(new Hand(cards[0], bid));
        }
        br.close();

        Collections.sort(hands);
        for (Hand hand : hands) {
            System.out.println(hand);
        }

        int total = 0;
        for(int i = 0; i < hands.size(); i++) {
            total+=hands.get(i).bid * (i+1);
        }

        System.out.println(total);
    }

}