"""Message Broker complete step consumer."""
import json
from amqpstorm import Message
from .utils.consumer import Consumer
from .utils.logger import LOG
import os


class CompleteConsumer(Consumer):
    """Complete Consumer class."""

    def handle_message(self, message: Message) -> None:
        """Handle message."""
        try:
            cmp_msg = json.loads(message.body)

            LOG.info(f"Completed message received: {cmp_msg} .")

        except Exception as error:
            LOG.error("Something went wrong: {0}".format(error))


def main() -> None:
    """Run the Complete consumer."""
    CONSUMER = CompleteConsumer(
        hostname=str(os.environ.get("BROKER_HOST")),
        port=int(os.environ.get("BROKER_PORT", 5670)),
        username=os.environ.get("BROKER_USER", "lega"),
        password=os.environ.get("BROKER_PASSWORD", ""),
        queue=os.environ.get("COMPLETED_QUEUE", "files.completed"),
        vhost=os.environ.get("BROKER_VHOST", "lega"),
    )
    CONSUMER.start()


if __name__ == "__main__":
    main()
