using System;
using System.IO;
using System.Net;
using System.Net.Mail;

class SmtpFacade
{
    public void Send(string From, string To, string Subject, string Body, Stream Attachment, string AttachmentMimeType)
    {
        using (var message = new MailMessage())
        {
            message.From = new MailAddress(From);
            message.To.Add(new MailAddress(To));
            message.Subject = Subject;
            message.Body = Body;

            if (Attachment != null)
            {
                var attachment = new Attachment(Attachment, "attachment", AttachmentMimeType);
                message.Attachments.Add(attachment);
            }

            using (var smtpClient = new SmtpClient("smtp.gmail.com", 587)) //"smtp.gmail.com"
            {
                smtpClient.EnableSsl = true;
                smtpClient.Credentials = new NetworkCredential("username", "password");

                smtpClient.Send(message);
            }
        }
    }
}

class Facade
{
    // static void Main(string[] args)
    // {
    //     var smtp = new SmtpFacade();

    //     string from = "sender@example.com";
    //     string to = "receiver@example.com";
    //     string subject = "Subject";
    //     string body = "Body";

    //     byte[] attachmentData = System.Text.Encoding.UTF8.GetBytes("Test attachment content"); //attachment as a stream
    //     using (var stream = new MemoryStream(attachmentData))
    //     {
    //         smtp.Send(from, to, subject, body, stream, "text/plain");
    //     }
    // }
}
