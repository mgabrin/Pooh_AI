import javafx.application.Application;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.concurrent.Worker;
import javafx.concurrent.Worker.State;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.scene.control.TitledPane;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;
import javafx.stage.Stage;
//  w  w  w.j av a2s  . c  o m
public class PoohDesktop extends Application {
  @Override
  public void start(final Stage stage) {
    stage.setWidth(1250);
    stage.setHeight(500);
    Scene scene = new Scene(new Group());


    final WebView browser = new WebView();
    final WebEngine webEngine = browser.getEngine();

    webEngine.getLoadWorker().stateProperty()
        .addListener(new ChangeListener<State>() {
          @Override
          public void changed(ObservableValue ov, State oldState, State newState) {

            if (newState == Worker.State.SUCCEEDED) {
              stage.setTitle(webEngine.getLocation());
            }

          }
        });
    webEngine.load("http://localhost:3000");

    scene.setRoot(browser);

    stage.setScene(scene);
    stage.show();
  }

  public static void main(String[] args) {
    launch(args);
  }
}
