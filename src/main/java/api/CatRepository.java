package api;

import java.util.List;

import org.springframework.data.repository.PagingAndSortingRepository;
import org.springframework.data.repository.query.Param;
import org.springframework.data.rest.core.annotation.RepositoryRestResource;

@RepositoryRestResource(collectionResourceRel = "cat", path = "cat")
public interface CatRepository extends PagingAndSortingRepository<Cat, Long> {

    List<Cat> findByColor(@Param("color") String color);
}
