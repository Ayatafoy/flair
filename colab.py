# !pip install -U git+https://github.com/NVIDIA/apex.git --no-cache-dir
#
# !pip install -U git+https://github.com/Ayatafoy/flair.git@fp-16-support
#
# # Authenticate to GCS.
# from google.colab import auth
#
# auth.authenticate_user()
# # Create the service client.
# from googleapiclient.discovery import build
#
# gcs_service = build('storage', 'v1')
#
# from apiclient.http import MediaIoBaseDownload
#
# bucket_name = 'jcp-search-pso'
# path_to_train = 'Aleksey/Flair train data/Product type classification/train.csv'
# path_to_test = 'Aleksey/Flair train data/Product type classification/test.csv'
# path_to_dev = 'Aleksey/Flair train data/Product type classification/dev.csv'
#
# with open('/tmp/train.csv', 'wb') as f:
#     request = gcs_service.objects().get_media(bucket=bucket_name,
#                                               object=path_to_train)
#     media = MediaIoBaseDownload(f, request)
#
#     done = False
#     while not done:
#         # _ is a placeholder for a progress object that we ignore.
#         # (Our file is small, so we skip reporting progress.)
#         _, done = media.next_chunk()
#
# with open('/tmp/test.csv', 'wb') as f:
#     request = gcs_service.objects().get_media(bucket=bucket_name,
#                                               object=path_to_test)
#     media = MediaIoBaseDownload(f, request)
#
#     done = False
#     while not done:
#         # _ is a placeholder for a progress object that we ignore.
#         # (Our file is small, so we skip reporting progress.)
#         _, done = media.next_chunk()
#
# with open('/tmp/dev.csv', 'wb') as f:
#     request = gcs_service.objects().get_media(bucket=bucket_name,
#                                               object=path_to_dev)
#     media = MediaIoBaseDownload(f, request)
#
#     done = False
#     while not done:
#         # _ is a placeholder for a progress object that we ignore.
#         # (Our file is small, so we skip reporting progress.)
#         _, done = media.next_chunk()
#
# print('Download complete')
#
# from flair.data_fetcher import NLPTaskDataFetcher
# from flair.embeddings import WordEmbeddings, FlairEmbeddings, DocumentLSTMEmbeddings
# from flair.models import TextClassifier
# from flair.trainers import ModelTrainer
# from pathlib import Path
#
# corpus = NLPTaskDataFetcher.load_classification_corpus(Path('/tmp/'), test_file='test.csv', dev_file='dev.csv', train_file='train.csv')
# word_embeddings = [WordEmbeddings('glove'), FlairEmbeddings('news-forward-fast'), FlairEmbeddings('news-backward-fast')]
# document_embeddings = DocumentLSTMEmbeddings(word_embeddings, hidden_size=128, reproject_words=True, reproject_words_dimension=64)
# classifier = TextClassifier(document_embeddings, label_dictionary=corpus.make_label_dictionary(), multi_label=False)
# trainer = ModelTrainer(classifier, corpus)
# trainer.train('./', max_epochs=20, mini_batch_size=8)