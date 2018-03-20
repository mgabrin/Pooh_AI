import javafx.application.Application;
import javafx.beans.value.ChangeListener;
import javafx.beans.value.ObservableValue;
import javafx.concurrent.Worker;
import javafx.concurrent.Worker.State;
import javafx.scene.Group;
import javafx.scene.Scene;
import javafx.stage.Screen;
import javafx.scene.control.TitledPane;
import javafx.scene.web.WebEngine;
import javafx.scene.web.WebView;
import javafx.stage.Stage;
import javafx.stage.StageStyle;
import javafx.geometry.Rectangle2D;
import javafx.scene.layout.Background;

public class PoohDesktop extends Application {
  @Override
  public void start(final Stage stage) {
    Rectangle2D primaryScreenBounds = Screen.getPrimary().getVisualBounds();

    stage.setWidth(400);
    stage.setHeight(200);
    stage.setX(primaryScreenBounds.getMaxX() *.6);
    stage.initStyle(StageStyle.UNDECORATED);
    Scene scene = new Scene(new Group());
    scene.setBackground(new Background(new BackgroundFill(Color
            .rgb(17, 119, 255), CornerRadii.EMPTY, Insets.EMPTY)));

    stage.setScene(scene);
    stage.show();
  }

  public static void main(String[] args) {
    launch(args);
  }
}
