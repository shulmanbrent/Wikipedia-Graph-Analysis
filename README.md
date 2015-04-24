Uses the request library and Beautiful soup to traverse to Perform a BFS search
on Wikipedia. However, this method is proving to be very slow. I believe that
this is because of the large number of get requests that I am making in order
to travers the links and the vast size of wikipedia.

To mitigate this I have dowloaded a data set from the Stanford Network Analysis
Project (SNAP). They have a corpus of all the html files of a limited quantity
of Wikipedia pages (approx 4000). I use this to apply my algorithm. In this way
I can limit the number of GET requests need, hopefully speeding up the process.
