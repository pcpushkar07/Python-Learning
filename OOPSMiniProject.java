import java.util.*;

public class OOPSMiniProject {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Enter received email:");
        String email = scanner.nextLine().toLowerCase();

        String reply = generateReply(email);
        System.out.println("\nSuggested Reply:\n");
        System.out.println(reply);

        scanner.close();
    }

    public static String generateReply(String email) {
        if (email.contains("meeting")) {
            return "Thank you for your email. I would be happy to attend the meeting. "
                    + "Please let me know the time and agenda.";

        } else if (email.contains("delay") || email.contains("late")) {
            return "Thank you for informing me. I understand the delay and appreciate your update. "
                    + "Please keep me posted on further progress.";

        } else if (email.contains("issue") || email.contains("problem") || email.contains("complaint")) {
            return "I'm sorry to hear about the issue. We are looking into it and will resolve it as soon as possible.";

        } else if (email.contains("thank")) {
            return "You're welcome! Glad I could help. Let me know if you need anything else.";

        } else if (email.contains("request")) {
            return "Thank you for your request. I will review it and get back to you shortly.";

        } else {
            return "Thank you for your email. I will review your message and respond accordingly.";
        }
    }
}