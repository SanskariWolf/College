Let's break down these questions and provide comprehensive answers with code examples where applicable.

**Q1. How does method resolution work in multiple inheritance when default methods are involved?**

In Java, direct multiple inheritance of classes is not allowed. However, interfaces can implement multiple inheritance by extending multiple interfaces, each of which can have default methods. This raises the question of method resolution when a class implements interfaces with conflicting default methods (methods with the same signature).

Here's how Java handles this situation:

1. **Class Implementation Takes Precedence:** If a class directly implements a method (overrides it), that implementation is always used.  This takes priority over any default method inherited from interfaces.

2. **Subinterface Takes Precedence:** If an interface extends other interfaces, and those interfaces contain a default method with the same signature, the default method defined in the *more specific* (i.e., deeper in the inheritance hierarchy) interface takes precedence.

3. **Conflict Resolution (Diamond Problem):** If two unrelated interfaces (not in a direct inheritance hierarchy) both provide a default method with the same signature, the implementing class *must* explicitly override the method and provide its own implementation.  Failing to do so results in a compile-time error.  The class can then *choose* to call one of the inherited default methods using the `InterfaceName.super.methodName()` syntax within its overridden method.

**Example:**

```java
interface InterfaceA {
    default void display() {
        System.out.println("InterfaceA: Display");
    }
}

interface InterfaceB {
    default void display() {
        System.out.println("InterfaceB: Display");
    }
}

interface InterfaceC extends InterfaceA {
    @Override
    default void display() {
        System.out.println("InterfaceC: Display");
    }
}

class MyClass implements InterfaceA, InterfaceB {  //Compile error - needs an override
    @Override
    public void display() {
       System.out.println("MyClass: Display"); // MyClass's implementation

       //Can call the default method if required like this
       InterfaceA.super.display();
    }
}


class MyOtherClass implements InterfaceC, InterfaceB {  //InterfaceC will take precedence over InterfaceA.

}

public class Main {
    public static void main(String[] args) {
        MyClass obj = new MyClass();
        obj.display(); // Output: MyClass: Display

        MyOtherClass obj2 = new MyOtherClass();
        obj2.display(); //Output: InterfaceC: Display
    }
}
```

Key takeaways:

*   Java avoids the ambiguity of direct multiple inheritance by enforcing explicit conflict resolution using overrides.
*   The `InterfaceName.super.methodName()` syntax allows a class to specifically invoke a default method inherited from a particular interface.

**Q2. XYZ Bank - Exception Handling**

```java
// Custom Exceptions
class InsufficientFundsException extends Exception {
    public InsufficientFundsException(String message) {
        super(message);
    }
}

class InvalidAccountException extends Exception {
    public InvalidAccountException(String message) {
        super(message);
    }
}


// Bank Account Class
class BankAccount {
    private String accountNumber;
    private double balance;

    public BankAccount(String accountNumber, double initialBalance) {
        this.accountNumber = accountNumber;
        this.balance = initialBalance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }


    public double getBalance() {
        return balance;
    }

    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited " + amount + " into account " + accountNumber);
    }

    public void withdraw(double amount) throws InsufficientFundsException {
        if (amount > balance) {
            throw new InsufficientFundsException("Insufficient funds in account " + accountNumber);
        }
        balance -= amount;
        System.out.println("Withdrawn " + amount + " from account " + accountNumber);
    }

    public void transfer(BankAccount recipient, double amount) throws InsufficientFundsException, InvalidAccountException {
        if (recipient == null) {
            throw new InvalidAccountException("Invalid recipient account.");
        }
        try {
            this.withdraw(amount);
            recipient.deposit(amount);
            System.out.println("Transferred " + amount + " from account " + accountNumber + " to account " + recipient.getAccountNumber());
        } catch (InsufficientFundsException e) {
            System.out.println("Transaction failed: " + e.getMessage());
            throw e; // Re-throw for higher-level handling, if necessary
        }
    }
}


public class BankTransaction {
    public static void main(String[] args) {
        BankAccount account1 = new BankAccount("12345", 1000.0);
        BankAccount account2 = new BankAccount("67890", 500.0);

        // Simulate insufficient funds
        try {
            account1.withdraw(1500.0);
        } catch (InsufficientFundsException e) {
            System.out.println("Withdrawal failed: " + e.getMessage());
        }

        // Simulate invalid account
        try {
            account1.transfer(null, 200.0);
        } catch (InsufficientFundsException | InvalidAccountException e) {
            System.out.println("Transfer failed: " + e.getMessage());
        }

        // Successful transfer
        try {
            account1.transfer(account2, 300.0);
        } catch (InsufficientFundsException | InvalidAccountException e) {
            System.out.println("Transfer failed: " + e.getMessage());
        }

        System.out.println("Account 1 balance: " + account1.getBalance());
        System.out.println("Account 2 balance: " + account2.getBalance());
    }
}
```

**Q3. Ride-Sharing App - Multithreading and Synchronization**

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Random;

// Custom Exception
class NoDriverAvailableException extends Exception {
    public NoDriverAvailableException(String message) {
        super(message);
    }
}


// Driver class
class Driver {
    private String driverId;
    private boolean isAvailable;

    public Driver(String driverId) {
        this.driverId = driverId;
        this.isAvailable = true;
    }

    public String getDriverId() {
        return driverId;
    }

    public boolean isAvailable() {
        return isAvailable;
    }

    public void setAvailable(boolean available) {
        isAvailable = available;
    }

    @Override
    public String toString() {
        return "Driver{" +
                "driverId='" + driverId + '\'' +
                ", isAvailable=" + isAvailable +
                '}';
    }
}

// Ride-Sharing System
class RideSharingSystem {
    private List<Driver> drivers = new ArrayList<>();

    public RideSharingSystem() {
        // Initialize some drivers
        drivers.add(new Driver("D1"));
        drivers.add(new Driver("D2"));
        drivers.add(new Driver("D3"));
    }


    // Method to find an available driver.  Using synchronization to prevent race condition
    public synchronized Driver findAvailableDriver() throws NoDriverAvailableException {
        for (Driver driver : drivers) {
            if (driver.isAvailable()) {
                driver.setAvailable(false); // Mark driver as unavailable
                return driver;
            }
        }
        throw new NoDriverAvailableException("No drivers are currently available.");
    }


    public synchronized void releaseDriver(Driver driver) {
        driver.setAvailable(true);
        System.out.println("Driver " + driver.getDriverId() + " released.");
    }

}


// Simulate a user requesting a ride
class UserRequest implements Runnable {
    private String userId;
    private RideSharingSystem rideSharingSystem;

    public UserRequest(String userId, RideSharingSystem rideSharingSystem) {
        this.userId = userId;
        this.rideSharingSystem = rideSharingSystem;
    }

    @Override
    public void run() {
        try {
            Driver driver = rideSharingSystem.findAvailableDriver();
            System.out.println("User " + userId + " assigned to driver " + driver.getDriverId());

            // Simulate the ride
            Thread.sleep(new Random().nextInt(5000));

            rideSharingSystem.releaseDriver(driver);

        } catch (NoDriverAvailableException e) {
            System.out.println("User " + userId + ": " + e.getMessage());
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}

public class RideSharing {

    public static void main(String[] args) {
        RideSharingSystem rideSharingSystem = new RideSharingSystem();

        // Simulate multiple users requesting rides concurrently
        Thread user1 = new Thread(new UserRequest("U1", rideSharingSystem));
        Thread user2 = new Thread(new UserRequest("U2", rideSharingSystem));
        Thread user3 = new Thread(new UserRequest("U3", rideSharingSystem));
        Thread user4 = new Thread(new UserRequest("U4", rideSharingSystem));
        Thread user5 = new Thread(new UserRequest("U5", rideSharingSystem));

        user1.start();
        user2.start();
        user3.start();
        user4.start();
        user5.start();


        //Demonstrating race condition without synchronization:
        //Imagine the drivers are first checked outside the synchronized method, and then they are set to unavailable inside
        //The check and the assignment are not atomic, therefore multiple users could find the same driver to be available
        //before one user could successfully change its state to unavailable.
    }
}
```

Key Improvements and Explanations:

*   **`synchronized` Keyword:**  The `findAvailableDriver()` method is synchronized.  This ensures that only one thread can access and modify the `drivers` list at a time.  This prevents multiple users from being assigned the same driver.  The `releaseDriver()` method is also synchronized.

*   **NoDriverAvailableException:**  This custom exception is thrown when all drivers are busy.  This is essential for handling the case where a user has to wait for a driver.

*   **Race Condition Example (Explained in Code Comments):** The race condition occurs because the availability check and the subsequent `setAvailable(false)` operation are *not atomic* without synchronization. Two threads could both see a driver as available *before* either one sets it to unavailable, leading to both threads getting the same driver.

*   **Realism:**  The `Thread.sleep()` simulates the duration of a ride.  The random duration adds some realism to the simulation.

*   **Resource Management:** The example shows how a driver is released back into the pool of available drivers after the ride is complete.

**Q4. Java Applet for Quiz UI**

```java
import java.applet.Applet;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.List;

//Custom Exception
class NoAnswerSelectedException extends Exception {
    public NoAnswerSelectedException(String message) {
        super(message);
    }
}

public class QuizApplet extends Applet implements ActionListener {

    private List<Question> questions;
    private int currentQuestionIndex = 0;
    private Label questionLabel;
    private Panel answerPanel;
    private Button submitButton;
    private String selectedAnswer = null; //Store the currently selected answer
    private Label resultLabel;


    @Override
    public void init() {
        // Initialize questions
        questions = new ArrayList<>();
        questions.add(new Question("What is the capital of France?", new String[]{"London", "Paris", "Berlin", "Rome"}, "Paris"));
        questions.add(new Question("What is 2 + 2?", new String[]{"3", "4", "5", "6"}, "4"));

        // UI components
        questionLabel = new Label();
        answerPanel = new Panel();
        answerPanel.setLayout(new GridLayout(0, 1)); //Vertical arrangement of radio buttons
        submitButton = new Button("Submit");
        resultLabel = new Label();

        submitButton.addActionListener(this);

        // Add components to applet
        setLayout(new BorderLayout());
        add(questionLabel, BorderLayout.NORTH);
        add(answerPanel, BorderLayout.CENTER);
        add(submitButton, BorderLayout.SOUTH);
        add(resultLabel, BorderLayout.EAST);

        displayQuestion();
    }

    private void displayQuestion() {
        Question currentQuestion = questions.get(currentQuestionIndex);
        questionLabel.setText(currentQuestion.getQuestionText());

        answerPanel.removeAll();  // Clear previous radio buttons
        ButtonGroup group = new ButtonGroup(); //Ensures only one radio button is selected

        for (String answer : currentQuestion.getAnswers()) {
            RadioButton radioButton = new RadioButton(answer);
            radioButton.addActionListener(e -> selectedAnswer = answer); //Set the selected answer
            group.add(radioButton); //Adds to the radiobutton group
            answerPanel.add(radioButton);
        }

        validate(); // Refresh the layout
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == submitButton) {
            try {
                checkAnswer();
            } catch (NoAnswerSelectedException ex) {
                resultLabel.setText(ex.getMessage());
            }
        }
    }

    private void checkAnswer() throws NoAnswerSelectedException {
        if (selectedAnswer == null){
            throw new NoAnswerSelectedException("No answer was selected.");
        }
        Question currentQuestion = questions.get(currentQuestionIndex);
        if (selectedAnswer.equals(currentQuestion.getCorrectAnswer())) {
            resultLabel.setText("Correct!");
        } else {
            resultLabel.setText("Incorrect.");
        }
        selectedAnswer = null; //Reset for next question

        currentQuestionIndex++;
        if (currentQuestionIndex < questions.size()) {
            displayQuestion();
        } else {
            questionLabel.setText("Quiz Complete!");
            answerPanel.removeAll();
            submitButton.setEnabled(false);
        }
    }

    // Inner class to represent a question
    class Question {
        private String questionText;
        private String[] answers;
        private String correctAnswer;

        public Question(String questionText, String[] answers, String correctAnswer) {
            this.questionText = questionText;
            this.answers = answers;
            this.correctAnswer = correctAnswer;
        }

        public String getQuestionText() {
            return questionText;
        }

        public String[] getAnswers() {
            return answers;
        }

        public String getCorrectAnswer() {
            return correctAnswer;
        }
    }
}
```

Key points:

*   **`NoAnswerSelectedException`:** Custom exception is thrown when the user submits without selecting an answer.
*   **`RadioButton` and `ButtonGroup`:** These are essential for multiple-choice questions. `ButtonGroup` ensures that only one radio button can be selected at a time.
*   **`ActionListener`:** Handles button clicks.
*   **Dynamic Question Display:** The `displayQuestion()` method dynamically updates the applet with the current question and answers.
*   **`validate()`:** Called to refresh the layout after adding or removing components.

**To run this applet:**

1.  **Save:** Save the code as `QuizApplet.java`.
2.  **Compile:** `javac QuizApplet.java`
3.  **Create an HTML file (e.g., `quiz.html`):**

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Quiz Applet</title>
    </head>
    <body>
        <applet code="QuizApplet.class" width="500" height="300">
        </applet>
    </body>
    </html>
    ```

4.  **Run:** Open the `quiz.html` file in a web browser with Java applet support (this might require older browsers or configurations, as applets are deprecated).

**Q5. Server-Client System with Sockets**

**(a) Roles of ServerSocket and Socket:**

*   **ServerSocket:**
    *   The `ServerSocket` is used by the *server* to listen for incoming connection requests from clients on a specific port.
    *   It essentially waits for clients to try to connect.
    *   When a client connects, the `ServerSocket` *accepts* the connection and creates a `Socket` object to handle the communication with that specific client.
    *   The `ServerSocket` is like a receptionist waiting for calls (client connection requests).

*   **Socket:**
    *   A `Socket` represents a single connection between a client and a server.
    *   On the *client* side, the `Socket` is created to initiate a connection to a specific server IP address and port number.
    *   On the *server* side, the `Socket` is created by the `ServerSocket` when it accepts a client connection.
    *   The `Socket` provides the input and output streams necessary for data transmission between the client and the server.
    *   The `Socket` is like the telephone line that allows two people to talk to each other.

**(b) InputStream and OutputStream for Data Transmission:**

*   **InputStream:**
    *   Used for *receiving* data.
    *   Both the client and server have `InputStream` objects associated with their respective `Socket` objects.
    *   The client's `InputStream` allows it to read data sent by the server.
    *   The server's `InputStream` allows it to read data sent by the client.
    *   You typically use methods like `read()`, `read(byte[])`, `BufferedReader.readLine()` (wrapped around the `InputStream`) to read data.

*   **OutputStream:**
    *   Used for *sending* data.
    *   Both the client and server have `OutputStream` objects associated with their respective `Socket` objects.
    *   The client's `OutputStream` allows it to send data to the server.
    *   The server's `OutputStream` allows it to send data to the client.
    *   You typically use methods like `write()`, `write(byte[])`, `PrintWriter.println()` (wrapped around the `OutputStream`) to send data.

**Example Code (Simplified):**

**Server.java**

```java
import java.io.*;
import java.net.*;

public class Server {
    public static void main(String[] args) {
        int port = 12345; // Choose a port number
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Server listening on port " + port);

            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                     PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                    System.out.println("Client connected: " + clientSocket.getInetAddress());

                    String message = in.readLine(); // Read from client's InputStream
                    System.out.println("Received from client: " + message);

                    String reversedMessage = new StringBuilder(message).reverse().toString();
                    out.println(reversedMessage);  // Send to client's OutputStream
                    System.out.println("Sent reversed message to client: " + reversedMessage);

                } catch (IOException e) {
                    System.err.println("Exception caught: " + e);
                }
            }
        } catch (IOException e) {
            System.err.println("Could not listen on port " + port + ": " + e);
        }
    }
}
```

**Client.java**

```java
import java.io.*;
import java.net.*;

public class Client {
    public static void main(String[] args) {
        String serverAddress = "localhost"; // Or the actual server IP address
        int port = 12345;

        try (Socket socket = new Socket(serverAddress, port);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
             BufferedReader stdIn = new BufferedReader(new InputStreamReader(System.in))) { //For reading input from console

            System.out.print("Enter message to send to server: ");
            String message = stdIn.readLine();
            out.println(message); // Send to server's OutputStream

            String response = in.readLine(); // Read from server's InputStream
            System.out.println("Server response: " + response);

        } catch (UnknownHostException e) {
            System.err.println("Don't know about host " + serverAddress);
        } catch (IOException e) {
            System.err.println("Couldn't get I/O for the connection to " + serverAddress);
        }
    }
}
```

Key points:

*   The `try-with-resources` statement ensures that the sockets and streams are automatically closed, even if exceptions occur.
*   `BufferedReader` and `PrintWriter` are used for easier text-based communication.  You could also use `DataInputStream` and `DataOutputStream` for binary data.
*   Error handling (using `try...catch`) is important for robust socket programming.

To run:

1.  Compile both `Server.java` and `Client.java`.
2.  Run `Server.java` first.  It will wait for a client connection.
3.  Run `Client.java`.  Enter a message in the console.
4.  The server will receive the message, reverse it, and send it back to the client. The client will display the reversed message.
