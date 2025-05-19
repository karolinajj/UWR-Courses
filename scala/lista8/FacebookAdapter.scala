import com.restfb._
import com.restfb.types.User
import scala.concurrent.{Future, ExecutionContext}
import java.io.{File, FileWriter}
import java.time.LocalDateTime
import Private._

object FacebookAdapter {

  private val myAppSecret: String = Private.appSecret

  class MyFacebookClient(currentAccessToken: String)
    extends DefaultFacebookClient(currentAccessToken, myAppSecret, Version.VERSION_5_0)

  def getUser(accessToken: String, id: String)(implicit ec: ExecutionContext): Future[User] = 
  Future {
    val client = new MyFacebookClient(accessToken)
    client.fetchObject(id, classOf[User])
  }

  def compareLikes(logFile: String, user1: String, user2: String, accessToken: String)(implicit ec: ExecutionContext): Future[Unit] = {
    val user1F = getUser(accessToken, user1)
    val user2F = getUser(accessToken, user2)

    for {
      //waits for u1 and u2 to complete
      u1 <- user1F
      u2 <- user2F
      writeToFile <- Future {
        val time = LocalDateTime.now()
        val line = s"$time $user1 $user2\n"
        val file = new File(logFile)
        val fw = new FileWriter(file, true)
        try fw.write(line)
        finally fw.close()
      }
    } yield {
        //runs after both threads are done
      val likes1 = Option(u1.getLikes).map(_.getTotalCount).getOrElse(0)
      val likes2 = Option(u2.getLikes).map(_.getTotalCount).getOrElse(0)
      println(s"${u1.getName}, likes: $likes1 , ${u2.getName}, likes: $likes2")
    }
  }
}
