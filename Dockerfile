FROM jupyter/tensorflow-notebook
WORKDIR /usr/src
EXPOSE 8889
ENTRYPOINT [ "jupyter", "notebook", "--ip=0.0.0.0", "--port=8889"]
