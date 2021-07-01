FROM nginx:alpine
RUN mkdir -p /etc/pki/certs/nginx
COPY ./certs /etc/pki/certs/nginx/
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 443
STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]

