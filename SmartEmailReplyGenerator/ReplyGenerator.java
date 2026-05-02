package SmartEmailReplyGenerator;

public class ReplyGenerator {
    public String generateReply(String category, Email originalEmail) {
        switch (category) {
            case "gratitude":
                return "You're welcome! I'm glad I could help.";
            case "meeting":
                return "Thank you for the update. I'll review the meeting details and get back to you.";
            case "inquiry":
                return "Thank you for your question. I'll look into this and respond shortly.";
            case "complaint":
                return "I'm sorry to hear about the issue. I'll investigate and resolve this as soon as possible.";
            default:
                return "Thank you for your email. I'll review it and respond accordingly.";
        }
    }
}