#include <iostream>
#include <string>
#include <thrift/protocol/TBinaryProtocol.h>
#include <thrift/transport/TSSLSocket.h>
#include <thrift/transport/TTransportUtils.h>
#include <thrift/transport/TTransport.h>
#include <thrift/transport/THttpClient.h>
#include <UserStore.h>
#include <NoteStore.h>

using namespace std;
using namespace apache::thrift;
using namespace apache::thrift::concurrency;
using namespace apache::thrift::protocol;
using namespace apache::thrift::transport;

int main() {
    string token =
        "S=s51:U=abc2b9:E=1608719cd46:C=1592f68a018:P=1cd:A=en-devtoken:V=2:H="
        "3c70ebbd4f60ba301e00b23ad92dab4d";

    boost::shared_ptr<TSSLSocketFactory> sslSocketFactory(
        new TSSLSocketFactory());
    sslSocketFactory->loadTrustedCertificates("./evernote.pem");
    boost::shared_ptr<TSSLSocket> sslSocket =
        sslSocketFactory->createSocket("app.yinxiang.com", 443);
    boost::shared_ptr<TBufferedTransport> bufferedTransport(
        new TBufferedTransport(sslSocket));
    boost::shared_ptr<TTransport> http_client(
        new THttpClient(bufferedTransport, "app.yinxiang.com", "/edam/note"));
    http_client->open();
    boost::shared_ptr<TBinaryProtocol> user_store_protocol(
        new TBinaryProtocol(http_client));
    evernote::edam::NoteStoreClient note_store(user_store_protocol,
                                               user_store_protocol);
    std::vector<evernote::edam::Notebook> note_books;
    note_store.listNotebooks(note_books, token);
}
