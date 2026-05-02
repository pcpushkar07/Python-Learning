package SmartEmailReplyGenerator;

public class EmailAnalyzer {
    public String analyze(Email email) {
        String content = email.getSubject() + " " + email.getBody().toLowerCase();

        if (content.contains("thank you") || content.contains("thanks")) {
            return "gratitude";
        } else if (content.contains("meeting") || content.contains("schedule")) {
            return "meeting";
        } else if (content.contains("question") || content.contains("help")) {
            return "inquiry";
        } else if (content.contains("complaint") || content.contains("problem")) {
            return "complaint";
        } else {
            return "general";
        }
    }
}