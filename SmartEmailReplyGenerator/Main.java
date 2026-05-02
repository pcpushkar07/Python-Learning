package SmartEmailReplyGenerator;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        EmailAnalyzer analyzer = new EmailAnalyzer();
        ReplyGenerator generator = new ReplyGenerator();
        Scanner scanner = new Scanner(System.in);

        System.out.println("Smart Email Reply Generator");
        System.out.println("Enter email details:");

        System.out.print("Sender: ");
        String sender = scanner.nextLine();

        System.out.print("Subject: ");
        String subject = scanner.nextLine();

        System.out.print("Body: ");
        String body = scanner.nextLine();

        Email email = new Email(subject, body, sender);
        String category = analyzer.analyze(email);
        String reply = generator.generateReply(category, email);

        System.out.println("\nOriginal Email:");
        System.out.println(email);
        System.out.println("\nSuggested Reply:");
        System.out.println(reply);

        scanner.close();
    }
}