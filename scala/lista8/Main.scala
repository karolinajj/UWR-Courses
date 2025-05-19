import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.{Success, Failure}
import com.restfb.DefaultFacebookClient
import com.restfb.Version
import com.restfb.types.User
import Private._

object MainApp {
  def main(args: Array[String]): Unit = {
    val accessToken =  Private.accessToken
    val appSecret: String = Private.appSecret

    //val client = new DefaultFacebookClient(accessToken, appSecret, Version.VERSION_5_0)
    val logFile = "compare_likes.log"

    val future = FacebookAdapter.compareLikes(logFile, Private.user1Id, Private.user2Id, accessToken)

    future.onComplete {
      case Success(_) => println("Comparison complete.")
      case Failure(ex) => println(s"Error occurred: ${ex.getMessage}")
    }

    //preventing immediate exit
    Thread.sleep(5000)
  }
}
