FROM 573841903179.dkr.ecr.us-east-1.amazonaws.com/nginx-wap:fakecert
RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/nginx.conf
ENTRYPOINT ["/docker-entrypoint.sh"]
EXPOSE 443
STOPSIGNAL SIGQUIT
CMD ["nginx", "-g", "daemon off;"]

