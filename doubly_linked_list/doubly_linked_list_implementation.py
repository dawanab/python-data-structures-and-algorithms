from doubly_linked_list import Node, DoublyLinkedList 

tinashePlaylist = DoublyLinkedList()
tinashePlaylist.add_to_head("Wanderer")
tinashePlaylist.add_to_head("Let Go")
tinashePlaylist.add_to_head("I Can See The Future")
tinashePlaylist.add_to_head("Looking 4 It")
tinashePlaylist.add_to_head("333")
print(tinashePlaylist.stringify_list())

tinashePlaylist.remove_tail()
print(tinashePlaylist.stringify_list())

tinashePlaylist.add_to_tail("Dreams Are Real")
tinashePlaylist.add_to_tail("Black Water")
tinashePlaylist.add_to_tail("Just A Taste")
tinashePlaylist.add_to_head("Middle Of Nowhere")
print(tinashePlaylist.stringify_list())

tinashePlaylist.remove_head()
print(tinashePlaylist.stringify_list())






